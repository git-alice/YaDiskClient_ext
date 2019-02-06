from YaDiskClient.YaDiskClient import YaDisk
import os

class YaDisk_ext(YaDisk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def preview(self, path_to_file, path_to_save_file, type_of_preview):
        """[Save preview of file]
        type_of_preview is string
        variables of type https://tech.yandex.com/disk/doc/dg/reference/preview-docpage/
        for ex: 'Xl', 'XS', '90', '90x', '90x180' """

        path_to_file = path_to_file + '?preview&size=' + type_of_preview
        resp = self._sendRequest("GET", path_to_file)
        if resp.status_code == 200:
            os.makedirs(os.path.dirname(path_to_save_file), exist_ok=True)
            with open(path_to_save_file, "wb") as f:
                f.write(resp.content)
        else:
            raise YaDiskException(resp.status_code, resp.content)
