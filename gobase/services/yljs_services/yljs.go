package yljs_services

import (
	"fmt"
	"syscall"
	"unicode/utf16"
	"unsafe"
)

func IntPtr(n int) uintptr {
	return uintptr(n)
}

func StrPtr(s string) uintptr {
	return uintptr(unsafe.Pointer(syscall.StringToUTF16Ptr(s)))
}

func StringToCharPtr(str string) *uint8 {
	chars := append([]byte(str), 0) // null terminated
	return &chars[0]
}

func StringToUTF16Ptr(str string) *uint16 {
	wchars := utf16.Encode([]rune(str + "\x00"))
	return &wchars[0]
}

var (
	dll = syscall.NewLazyDLL("dlls\\igkmlib32.dll")
)

type YLJSService struct {
	dll *syscall.LazyDLL
}

func New() (yljs *YLJSService, err error) {
	return &YLJSService{dll: dll}, nil
}

func (yljs YLJSService) Release() (uintptr, uintptr, error) {
	Release := yljs.dll.NewProc("Release")
	r1, r2, err := Release.Call(0, 0)
	return r1, r2, err
}

func (yljs YLJSService) GetModel() string {
	Release := yljs.dll.NewProc("GetSerialNumber")
	r1, _, _ := Release.Call()

	p := (*byte)(unsafe.Pointer(r1))
	// define a slice to fill with the p string
	data := make([]byte, 0)

	// loop until find '\0'
	for *p != 0 {
		data = append(data, *p)         // append 1 byte
		r1 += unsafe.Sizeof(byte(0))    // move r to next byte
		p = (*byte)(unsafe.Pointer(r1)) // get the byte value
	}
	name := string(data) // convert to Golang string
	fmt.Println(name)
	//print(string(*ptr))
	//stringPtr := (*string)(ptr)
	//
	//
	//newData := *stringPtr

	//Got it:
	//fmt.Println(newData)
	return name
}

func (yljs YLJSService) MoveMouseTo(x int, y int) (uintptr, uintptr, error) {
	MoveMouseTo := yljs.dll.NewProc("MoveMouseTo")
	r1, r2, err := MoveMouseTo.Call(IntPtr(x), IntPtr(y))
	return r1, r2, err
}
