from litex.soc.tools.remote import RemoteClient
from control_prbs import *

wb = RemoteClient()
wb.open()
prcon = PRBSControl(wb.regs,"top_gtp")
prcon.phaseAlign()
prcon.setErrMask(0,20)
prcon.setPRBSConfig(7,7)
print(prcon.calcBERabs(5,20))
prcon.setErrMask(0.5,20)
print(prcon.calcBERabs(5,20))
prcon.resetTx()
prcon.resetRx()
prcon.phaseAlign()

prcon.setPRBSConfig(7,7)
print(prcon.calcBERabs(5,20))
prcon.setErrMask(0.5,20)
print(prcon.calcBERabs(5,20))

prcon.PLLlockStatus()

