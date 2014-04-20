from provider import CDNProvider


class Sina(CDNProvider):
    base_url = "//lib.sinaapp.com/%(file_type)s/%(lib_name)s/%(version)s/js/%(lib_name)s.min.%(file_type)s"

    def build_js_url_with_dict(self, lib_name, version, file_type="js"):
        return self.base_url % {"lib_name": lib_name, "version": version, "file_type": file_type}

    def bootstrap(self, version):
        return self.build_js_url_with_dict("bootstrap", version)

    def bootstrap_css(self, version):
        return self.build_js_url_with_dict("bootstrap", version, "css")

    def jquery(self, version):
        return self.build_js_url_with_dict("jquery", version)