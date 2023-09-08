import os

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


class GDrive:
    def __init__(
        self,
        filePath="service-secrets.json",
        out_folder_id="1DczeASlw9bvxW7nvOMQZ3RdJcBg96GmQ",
        input_folder_id="1hk4pw0CwSkUjsM_4OTX9FEE0k73qI4qd",
    ):
        self._auth = self.login_with_service_account(filePath)
        self._drive = GoogleDrive(self._auth)
        self._out_folder = out_folder_id
        self._input_folder = input_folder_id

    def login_with_service_account(self, filePath):
        settings = {
            "client_config_backend": "service",
            "service_config": {
                "client_json_file_path": filePath,
            },
        }
        gauth = GoogleAuth(settings=settings)
        gauth.ServiceAuth()
        return gauth

    def upload_file(
        self,
        file_name,
    ):  # 1DczeASlw9bvxW7nvOMQZ3RdJcBg96GmQ
        try:
            new_file = self._drive.CreateFile(
                {"parents": [{"id": self._out_folder}]}
            )  # Create GoogleDriveFile instance with title 'Hello.txt'.
            new_file.SetContentFile(file_name)
            new_file.Upload()
            print(new_file["title"])
            return {"result": "OK"}
        except Exception as e:
            print(e)
            return {"result": "Failed", "error": e}

    def download_file(self, filePath):
        try:
            result_id = self.get_id_of_title("melody.mid", self._input_folder)
            file2 = self._drive.CreateFile({"id": result_id})
            file2.GetContentFile(filePath)
            return {"result": result_id}
        except Exception as e:
            print(e)
            return {"result": "Failed", "error": e}

    def get_id_of_title(self, title, parent_directory_id):
        foldered_list = self._drive.ListFile(
            {"q": "'" + parent_directory_id + "' in parents and trashed=false"}
        ).GetList()
        for file in foldered_list:
            if file["title"] == title:
                return file["id"]
            return None
