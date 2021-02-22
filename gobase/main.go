package main

import (
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/cors"
	"gobase/controllers/damo_controllers"
	"gobase/controllers/yljs_controllers"
	"gobase/services/damo_services"
	"gobase/services/yljs_services"
	"os"
)

func main() {
	// 创建大漠插件实例
	pwd, _ := os.Getwd()
	damo_services.SetDllPathW(pwd+"\\dlls\\dm.dll", 0)
	damo, _ := damo_services.New()
	yljs, _ := yljs_services.New()

	defer damo.Release()
	defer yljs.Release()

	app := fiber.New()
	app.Use(cors.New())

	api := app.Group("/api")

	damo_controllers.Init(api, damo)
	yljs_controllers.Init(api, yljs)

	_ = app.Listen(":8801")
}
