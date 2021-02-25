#include "damo.h"

  // WinExec("regsvr32.exe dm.dll/s", SW_SHOW); // 运行注册插件命令
HRESULT _coInitialized = CoInitialize(NULL);  // 初始化 COM 库
CLSID clsid;                                  // COM 对象标识符
HRESULT _cLSIDFromProgID = CLSIDFromProgID(OLESTR("dm.dmsoft"), &clsid);
CComPtr<Idmsoft> dm;
HRESULT _coCreateInstance = dm.CoCreateInstance(clsid);

std::string runDm() {
  std::string ver(dm->Ver());
  std::cout << ver << std::endl;
  return ver;
}