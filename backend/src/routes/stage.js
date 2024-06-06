const express = require("express");
const router = express.Router();
const StageController = require("../controller/stage.js");

router.get("/", StageController.getAllLevel);

router.get("/:stage_id", StageController.getDetailLevel);

module.exports = router;
