#include "damo.h"

  // WinExec("regsvr32.exe dm.dll/s", SW_SHOW); // ����ע��������
HRESULT _coInitialized = CoInitialize(NULL);  // ��ʼ�� COM ��
CLSID clsid;                                  // COM �����ʶ��
HRESULT _cLSIDFromProgID = CLSIDFromProgID(OLESTR("dm.dmsoft"), &clsid);
CComPtr<Idmsoft> dm;
HRESULT _coCreateInstance = dm.CoCreateInstance(clsid);

std::string runDm() {
  std::string ver(dm->Ver());
  std::cout << ver << std::endl;
  return ver;
}