#---------------------------------------------------------------------------
# 参照

import glob
import json
from xoxxox.shared import PrcFlw
from xoxxox.libmid import LibMid
from xoxxox.params import Config
from xoxxox.params_cmf import CnfCmf

#---------------------------------------------------------------------------
# 処理：ＧＵＩワークフロー環境向け

class AppCmf:

  # サーバのアドレス群の辞書を返す（文字列（JSON形式））
  @staticmethod
  def dicsrv():
    dicsrv=PrcFlw.dicsrv()
    datres = json.dumps(dicsrv).encode("utf-8")
    return datres

  # ワークフローのオプション群の辞書を返す（文字列（JSON形式））
  @staticmethod
  def diccmf():
    diccmf=AppCmf.getcmf()
    datres = json.dumps(diccmf).encode("utf-8")
    return datres

  def getcmf():
    diccnf = {}
    lstpth = glob.glob(Config.dircnf + "/" + CnfCmf.glbcmf)
    for pthcnf in lstpth:
      with open(pthcnf, "r") as f:
        d = json.load(f)
        for key, lst in d.items():
          if key in diccnf:
            diccnf[key].extend(lst)
          else:
            diccnf[key] = lst
    return diccnf

LibMid.dicprc["xoxxox.AppCmf.diccmf"] = {"frm": "xoxxox_libcmf.AppCmf.diccmf", "syn": True}
LibMid.dicprc["xoxxox.AppCmf.dicsrv"] = {"frm": "xoxxox_libcmf.AppCmf.dicsrv", "syn": True}
