#!/usr/bin/perl
# textos.pl : lit les textos (iMessage et SMS) d'un Mac, en lecture seule.
# VERSION 1.8.0
#
# Fourni par la trousse OSE, competences ma-voix et clients-dormants.
# Ne modifie rien, n'envoie rien. Lit ~/Library/Messages/chat.db avec
# l'outil sqlite3 du Mac, et les noms dans le carnet de Contacts.
#
# Demande l'Acces complet au disque pour l'application Claude
# (Reglages Systeme, Confidentialite et securite, Acces complet au disque).
#
# Deux modes :
#   envoyes  <mois>             les textos ECRITS PAR LE COURTIER, texte seulement,
#                               sans numero ni nom : la matiere de sa voix
#   projets  <mois> [--groupes] [mots...]
#                               les conversations ou LE CONTACT a parle de vendre,
#                               d'acheter ou de la valeur de sa maison, une fiche
#                               par conversation : nom, numero, dates, qui a ecrit
#                               en dernier, extraits. Sans --groupes, les
#                               conversations de groupe sont laissees de cote.
#   bilan                       ce qui est lisible, sans rien montrer du contenu
#
# Piege connu : depuis macOS 13, une partie des textos n'a plus son texte dans
# la colonne `text`. Il est encode dans `attributedBody`. Ce lecteur lit les deux.

use strict;
use warnings;
use utf8;
use Encode qw(decode encode);

binmode(STDOUT, ':encoding(UTF-8)');
binmode(STDERR, ':encoding(UTF-8)');

my $HOME = $ENV{HOME} || '';
my $DB   = "$HOME/Library/Messages/chat.db";
my $SEP  = "\x1f";
my $FIN  = "\x1e";
my $EPOQUE_APPLE = 978307200;
my $GROUPES = 0;

# Des mots d'INTENTION, pas de metier : un courtier parle de visites et de
# proprietes toute la journee avec ses collegues. Ce qui compte, c'est le
# contact qui dit qu'il veut vendre, acheter ou savoir ce que vaut sa maison.
my @MOTS_DEFAUT = (
    'vendre', 'vends', 'mettre en vente', 'vente de (?:ma|notre|la)',
    'acheter', "achat d'(?:une|un)", 'premi[eè]re maison', 'premier achat',
    '[ée]valuation', '[ée]valuer (?:ma|notre)', 'combien vaut', 'combien (?:je|on) (?:pourrai[st]|peut) (?:avoir|obtenir)',
    'valeur de (?:ma|notre) (?:maison|propri|condo)',
    'pr[ée]-?approb', 'pr[ée]-?autoris', 'hypoth[eè]que',
    'd[ée]m[ée]nager', 'plus grand', 'plus petit',
    'sell', 'selling', 'buy (?:a|our|my)', 'buying', 'list (?:our|my) (?:house|condo|home)',
    'what.{0,10}worth', 'mortgage', 'pre-?approv', 'move out', 'downsiz',
);

sub meurt {
    my ($msg) = @_;
    print STDERR "$msg\n";
    exit 1;
}

sub sqlite {
    my ($db, $sql) = @_;
    my @cmd = ('sqlite3', '-readonly', '-batch', '-noheader',
               '-separator', $SEP, '-newline', $FIN, $db, $sql);
    open(my $fh, '-|', @cmd) or return undef;
    binmode($fh, ':raw');
    local $/;
    my $brut = <$fh>;
    close($fh);
    return undef if $? != 0;
    $brut = '' unless defined $brut;
    my @lignes;
    for my $l (split /$FIN/, $brut) {
        next unless length $l;
        push @lignes, [ split /$SEP/, $l, -1 ];
    }
    return \@lignes;
}

sub verifier_acces {
    meurt("PAS-DE-MAC : ce lecteur ne fonctionne que sur un Mac.") unless $^O eq 'darwin';
    meurt("PAS-DE-TEXTOS : aucun fichier de Messages sur ce Mac.") unless -e $DB;
    my $t = sqlite($DB, 'select count(*) from message;');
    meurt("ACCES-REFUSE : l'application Claude n'a pas l'Acces complet au disque.")
        unless defined $t && @$t;
}

# Texte d'un message : la colonne text, sinon attributedBody decode.
sub texte_attribue {
    my ($hex) = @_;
    return '' unless defined $hex && length $hex;
    my $b = pack('H*', $hex);
    my $i = index($b, 'NSString');
    return '' if $i < 0;
    my $j = index($b, '+', $i + 8);
    return '' if $j < 0 || $j > $i + 20;
    my $p = $j + 1;
    my $n = ord(substr($b, $p, 1));
    $p++;
    if ($n == 0x81) {
        $n = unpack('v', substr($b, $p, 2));
        $p += 2;
    } elsif ($n == 0x82) {
        $n = unpack('V', substr($b, $p, 3) . "\0");
        $p += 3;
    }
    my $t = eval { decode('UTF-8', substr($b, $p, $n), Encode::FB_CROAK) };
    return defined $t ? $t : '';
}

sub texte_de {
    my ($text, $hex) = @_;
    my $t = (defined $text && length $text)
        ? (eval { decode('UTF-8', $text) } // '')
        : texte_attribue($hex);
    $t =~ s/\x{FFFC}//g;
    $t =~ s/\s+/ /g;
    $t =~ s/^ | $//g;
    return $t;
}

sub limite_ns {
    my ($mois) = @_;
    $mois = 6 unless defined $mois && $mois =~ /^\d+$/ && $mois > 0;
    my $s = time() - int($mois * 30.44 * 86400) - $EPOQUE_APPLE;
    return $s * 1_000_000_000;
}

sub date_de {
    my ($d) = @_;
    return '' unless defined $d && $d =~ /^-?\d+$/;
    my $s = $d > 1_000_000_000_000 ? int($d / 1_000_000_000) : $d;
    my @t = localtime($s + $EPOQUE_APPLE);
    return sprintf('%04d-%02d-%02d', $t[5] + 1900, $t[4] + 1, $t[3]);
}

# 10 derniers chiffres d'un numero, pour relier un texto a une fiche Contacts.
sub cle_numero {
    my ($n) = @_;
    return '' unless defined $n;
    return lc($n) if $n =~ /\@/;
    (my $c = $n) =~ s/\D//g;
    return length($c) >= 10 ? substr($c, -10) : $c;
}

sub carnet {
    my %nom;
    for my $f (glob("'$HOME/Library/Application Support/AddressBook/Sources/'*'/AddressBook-v22.abcddb'"),
               glob("'$HOME/Library/Application Support/AddressBook/AddressBook-v22.abcddb'")) {
        my $sql = q{
            select coalesce(r.ZFIRSTNAME,''), coalesce(r.ZLASTNAME,''),
                   coalesce(r.ZORGANIZATION,''), p.ZFULLNUMBER
            from ZABCDPHONENUMBER p join ZABCDRECORD r on p.ZOWNER = r.Z_PK
            union all
            select coalesce(r.ZFIRSTNAME,''), coalesce(r.ZLASTNAME,''),
                   coalesce(r.ZORGANIZATION,''), e.ZADDRESS
            from ZABCDEMAILADDRESS e join ZABCDRECORD r on e.ZOWNER = r.Z_PK;
        };
        my $l = sqlite($f, $sql) or next;
        for my $r (@$l) {
            my ($p, $n, $o, $num) = map { eval { decode('UTF-8', $_ // '') } // '' } @$r;
            my $nom = join(' ', grep { length } $p, $n);
            $nom = $o unless length $nom;
            my $k = cle_numero($num);
            $nom{$k} //= $nom if length $k && length $nom;
        }
    }
    return \%nom;
}

my $SQL_BASE = q{
    select m.date, m.is_from_me, coalesce(h.id, ''), coalesce(c.chat_identifier, ''),
           coalesce(c.style, 45), coalesce(c.display_name, ''),
           m.text, hex(m.attributedBody)
    from message m
    left join handle h on m.handle_id = h.ROWID
    left join chat_message_join j on j.message_id = m.ROWID
    left join chat c on c.ROWID = j.chat_id
    where m.date > %s
      and coalesce(m.associated_message_type, 0) = 0
      and (m.text is not null or m.attributedBody is not null)
      %s
    order by m.date;
};

sub mode_envoyes {
    my ($mois) = @_;
    verifier_acces();
    my $l = sqlite($DB, sprintf($SQL_BASE, limite_ns($mois), 'and m.is_from_me = 1'))
        or meurt("LECTURE-IMPOSSIBLE : la base de Messages n'a pas pu etre lue.");
    my %vu;
    my $n = 0;
    for my $r (@$l) {
        my ($date, undef, undef, undef, $style, undef, $text, $hex) = @$r;
        my $t = texte_de($text, $hex);
        next if length($t) < 15;                  # « Ok », « Merci! » : rien a apprendre
        next if $t =~ m{^https?://\S+$};          # un lien seul
        next if $vu{$t}++;                        # un message copie-colle plusieurs fois
        my $type = ($style == 43) ? 'groupe' : 'seul';
        print date_de($date), "\t$type\t$t\n";
        $n++;
    }
    print STDERR "$n textos envoyes retenus.\n";
}

sub mode_projets {
    my ($mois, @mots) = @_;
    if (@mots && $mots[0] eq '--groupes') { $GROUPES = 1; shift @mots }
    verifier_acces();
    @mots = @MOTS_DEFAUT unless @mots;
    my $motif = join('|', @mots);
    my $re = qr/(?:$motif)/i;
    my $noms = carnet();
    my $l = sqlite($DB, sprintf($SQL_BASE, limite_ns($mois), ''))
        or meurt("LECTURE-IMPOSSIBLE : la base de Messages n'a pas pu etre lue.");

    my (%conv, @ordre);
    for my $r (@$l) {
        my ($date, $moi, $handle, $chat, $style, $titre, $text, $hex) = @$r;
        my $cle = length $chat ? $chat : $handle;
        next unless length $cle;
        my $c = $conv{$cle} //= do {
            push @ordre, $cle;
            { cle => $cle, groupe => ($style == 43), titre => $titre,
              personnes => {}, n => 0, extraits => [] }
        };
        my $t = texte_de($text, $hex);
        next unless length $t;
        $c->{personnes}{$handle} = 1 if length $handle && !$moi;
        $c->{premier} //= date_de($date);
        $c->{dernier} = date_de($date);
        $c->{dernier_de} = $moi ? 'courtier' : 'contact';
        $c->{n}++;
        if ($t =~ $re) {
            $c->{signal}++ unless $moi;
            if (@{ $c->{extraits} } < 5) {
                my $x = length($t) > 240 ? substr($t, 0, 240) . '...' : $t;
                push @{ $c->{extraits} }, date_de($date) . ' ' . ($moi ? 'MOI' : 'LUI') . " : $x";
            }
        }
    }

    my $k = 0;
    for my $cle (@ordre) {
        my $c = $conv{$cle};
        next unless $c->{signal};                 # le contact lui-meme en a parle
        next if $c->{groupe} && !$GROUPES;        # les groupes : seulement sur demande
        my @qui = sort keys %{ $c->{personnes} };
        @qui = ($cle) unless @qui;
        my @noms = map { $noms->{ cle_numero($_) } // '' } @qui;
        $k++;
        print "=== CONVERSATION $k", ($c->{groupe} ? ' (groupe)' : ''), "\n";
        print "Nom : ", join(', ', grep { length } @noms) || ($c->{titre} || '(pas dans les Contacts)'), "\n";
        print "Numero ou adresse : ", join(', ', @qui), "\n";
        print "Premier message : $c->{premier}   Dernier : $c->{dernier}   Dernier mot : $c->{dernier_de}   Messages : $c->{n}\n";
        print "  $_\n" for @{ $c->{extraits} };
        print "\n";
    }
    print STDERR "$k conversations ou un projet immobilier revient.\n";
}

sub mode_bilan {
    verifier_acces();
    my $l = sqlite($DB, q{
        select count(*), sum(is_from_me),
               sum(case when text is null and attributedBody is not null then 1 else 0 end)
        from message where coalesce(associated_message_type, 0) = 0;
    });
    my ($tous, $moi, $codes) = @{ $l->[0] };
    my $l2 = sqlite($DB, sprintf($SQL_BASE, limite_ns(1200), 'and m.text is null and m.is_from_me = 1'));
    my ($ok, $rate) = (0, 0);
    for my $r (@{ $l2 || [] }) {
        length(texte_attribue($r->[7])) ? $ok++ : $rate++;
    }
    my $noms = carnet();
    print "Textos lisibles : $tous, dont $moi envoyes par vous.\n";
    print "Textos au format encode : $codes; lus par ce lecteur : $ok, illisibles : $rate.\n";
    print "Fiches Contacts reliables : ", scalar(keys %$noms), ".\n";
}

my $mode = shift @ARGV // '';
if    ($mode eq 'envoyes') { mode_envoyes(@ARGV) }
elsif ($mode eq 'projets') { mode_projets(@ARGV) }
elsif ($mode eq 'bilan')   { mode_bilan() }
else  { meurt("Usage : perl textos.pl envoyes <mois> | projets <mois> [--groupes] [mots...] | bilan") }
exit 0;
