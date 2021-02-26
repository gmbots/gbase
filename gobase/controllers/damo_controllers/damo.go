package damo_controllers

import (
	"fmt"
	"github.com/gofiber/fiber/v2"
	"gobase/services/damo_services"
)

var dm *damo_services.DamoService

func Init(api fiber.Router, _dm *damo_services.DamoService) {
	dm = _dm
	dmApi := api.Group("/damo")
	dmApi.Get("/Ver", ver)
}

// 版本号
func ver(c *fiber.Ctx) error {
	fmt.Println(c.Query("id"))
	return c.JSON(fiber.Map{
		"message": dm.Ver(),
	})
}
