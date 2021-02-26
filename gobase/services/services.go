package services

import (
	"gobase/services/damo_services"
	"gobase/services/yljs_services"
)

type Resource struct {
	DamoService damo_services.DamoService
	YLJSService yljs_services.YLJSService
}

var UserServicesMapping = map[string]Resource{}
