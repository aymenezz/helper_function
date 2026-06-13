from google.colab import drive
import sys
import os
import subprocess
class install:
  def __init__(self,name_package=None):
    self.name_package=name_package
    self.package_path='/content/drive/MyDrive/colab_packages'
  def install_package(self):
      drive.mount('/content/drive')
      # package_path = '/content/drive/MyDrive/colab_packages'
      os.makedirs(self.package_path, exist_ok=True)
      sys.path.insert(0, self.package_path)
      subprocess.check_call([
            sys.executable, 
            "-m", 
            "pip", 
            "install", 
            "--target", 
            self.package_path, 
            self.name_package
        ])
      return f'Successfully installed {self.name_package} to {self.package_path}'
  def call_package(self):
      drive.mount('/content/drive')
      package_path = '/content/drive/MyDrive/colab_packages'
      os.makedirs(package_path, exist_ok=True)
      sys.path.insert(0, package_path)
