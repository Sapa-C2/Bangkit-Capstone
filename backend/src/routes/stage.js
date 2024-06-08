const express = require("express");
const router = express.Router();
const UserController = require("../controller/stage.js");

router.get("/", UserController.getAllStages);

router.get("/:stage_id", UserController.getDetailStage);

module.exports = router;
