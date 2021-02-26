// +build windows
// export GOARCH=386

package damo_services

import (
	"os"
	"syscall"
	"unsafe"

	ole "github.com/go-ole/go-ole"
	"github.com/go-ole/go-ole/oleutil"
)

var pwd, _ = os.Getwd()

var (
	dmReg32         = syscall.NewLazyDLL(pwd + "\\dlls\\DmReg.dll")
	procSetDllPathA = dmReg32.NewProc("SetDllPathA")
	procSetDllPathW = dmReg32.NewProc("SetDllPathW")
)

// 大漠类型申明
type DamoService struct {
	dm       *ole.IDispatch
	IUnknown *ole.IUnknown
}

// 初始化实例
func New() (dm *DamoService, err error) {
	var com DamoService
	// 创建对象
	_ = ole.CoInitialize(0)
	com.IUnknown, err = oleutil.CreateObject("dm.dmsoft")
	if err != nil {
		return nil, err
	}
	// 查询接口
	com.dm, err = com.IUnknown.QueryInterface(ole.IID_IDispatch)
	if err != nil {
		return nil, err
	}
	return &com, nil
}

// Release 释放
func (com *DamoService) Release() {
	com.IUnknown.Release()
	com.dm.Release()
	ole.CoUninitialize()
}

// 注册插件
func SetDllPathA(path string, mode int) bool {
	var _p0 *uint16
	_p0, _ = syscall.UTF16PtrFromString(path)
	ret, _, _ := syscall.Syscall(procSetDllPathA.Addr(), 2, uintptr(unsafe.Pointer(_p0)), uintptr(mode), 0)
	return ret != 0
}

// 注册插件
func SetDllPathW(path string, mode int) bool {
	var _p0 *uint16
	_p0, _ = syscall.UTF16PtrFromString(path)
	ret, _, _ := syscall.Syscall(procSetDllPathW.Addr(), 2, uintptr(unsafe.Pointer(_p0)), uintptr(mode), 0)
	return ret != 0
}

// 版本号
func (com *DamoService) Ver() string {
	ver, _ := com.dm.CallMethod("Ver")
	return ver.ToString()
}
