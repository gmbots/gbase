package yljs_controllers

import (
	"github.com/gofiber/fiber/v2"
	"gobase/services/yljs_services"
	"strconv"
)

var yljs *yljs_services.YLJSService

func Init(api fiber.Router, _yljs *yljs_services.YLJSService) {
	yljs = _yljs
	dmApi := api.Group("/yljs")
	dmApi.Get("/GetModel", getModel)
	dmApi.Get("/MoveMouseTo/:x/:y", moveMouseTo)
}

// 版本号
func getModel(c *fiber.Ctx) error {
	return c.JSON(fiber.Map{
		"message": yljs.GetModel(),
	})
}
func moveMouseTo(c *fiber.Ctx) error {
	x, err := strconv.ParseInt(c.Params("x"), 10, 64)
	if err != nil {
		return c.JSON(fiber.Map{
			"message": "X is absent",
		})
	}
	y, err := strconv.ParseInt(c.Params("y"), 10, 32)
	if err != nil {
		return c.JSON(fiber.Map{
			"message": "y is absent",
		})
	}
	yljs.MoveMouseTo(int(x), int(y))

	return c.JSON(fiber.Map{
		"message": "Ok",
	})
}
