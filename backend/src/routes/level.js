const express = require("express");
const router = express.Router();
const UserController = require('../controller/level.js');

router.get('/', UserController.getAllLevel);

router.get('/:level_id', UserController.getDetailLevel);


module.exports = router;