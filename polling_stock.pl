use LWP 5.64; # Loads all important LWP classes, and makes
              #  sure your version is reasonably recent.

# stock list.
# shanghai prefix is 'sha';
# shenzhen and chuangye prefix is 'she'

my @stocks=("sha:000001","she:399001","she:002179","sha:600478","she:002025",,"she:000799","sha:600867","she:000895");
my $stockstring= join "," , @stocks;

my $url="http://finance.google.com.cn/finance/info?client=ig&q=".$stockstring;
my $proxy='http://127.0.0.1:8080/';

my $browser = LWP::UserAgent->new();


my ($sec,$min,$hour,$mday,$mon,$year,
          $wday,$yday,$isdst) = localtime(time);

system("cls");

while(1) {

    my $response = $browser->get( $url );
        #print $url;
    $response->is_success or
    print "Can't get $url " unless $response->is_success;
    my $content=$response->as_string;

    system("cls");
    printf("Google Finance Stock Information.\nGet Data on %d-%d-%d\n",$year+1900,$mon+1,$mday);
    printf "Stock_Num,    Cur_Pri,     Change_Per,    Chg_Pri,        Time\n";
    my @values=($content=~/\{.*?\}/sig);

    my $count=1;
    foreach $value (@values) {
        #print $value;
        my @subvalues= ($value=~/\"(.*?)\"/sig);
        printf (" %6s,   %10s,   %10s,   %10s%%,   %10s\n",$subvalues[3],$subvalues[7],$subvalues[21],$subvalues[25],$subvalues[19])
;
        $count++;
    }

    # Interval
    sleep(60);

}
