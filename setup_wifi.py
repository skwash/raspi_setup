import sys
from jinja2 import Template

tmplfile = "wpa_supplicant.tmpl"


def make_wpa_supplicant(tmpl_file, ssid, password):
    params = {'ssid': ssid, 'password': password}
    f = open(tmpl_file, "r")

    template = Template(f.read())
    return template.render(params)


def main(ssid, password):

    outfile = "wpa_supplicant.conf"

    contents = make_wpa_supplicant(tmplfile, ssid, password)

    f = open(outfile, "w+")
    f.write(contents)
    f.close()


def usage():
    return "Usage: python setup_wifi.py <ssid> <password>\n"


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print usage()
        sys.exit()

    main(sys.argv[1], sys.argv[2])
