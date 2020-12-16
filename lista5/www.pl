use HTTP::Daemon;
use HTTP::Status;  

my $d = HTTP::Daemon->new || die;
print "Please contact me at: ", $d->url, "\n";


while (my $c = $d->accept) {
    while (my $r = $c->get_request) {
        if ($r->method eq 'GET') {
            $path = $r->uri->path;

            if (index($path, "/ts") == 0) {
                $real_path = "./website/ts";
                if (index($path, "/lista") == 3) {
                    $real_path = $real_path . "/listy/" . substr($path, 4) . ".html";
                    $c->send_file_response($real_path);
                }
                elsif (length($path) == 3) {
                    $real_path = $real_path . "/ts.html";
                    $c->send_file_response($real_path);
                }
                else {
                    $c->send_error(RC_FORBIDDEN);
                }
            }
            elsif (index($path, "/aisd") == 0 && length($path) == 5) {
                $c->send_file_response("./website/aisd/aisd.html");
            }
            elsif (length($path) == 1) {
                $c->send_file_response("./website/index.html");
            }
            else {
                $c->send_error(RC_FORBIDDEN);
            }
        }
        else {
            $c->send_error(RC_FORBIDDEN);
        }
    }
    $c->close;
    undef($c);
}

