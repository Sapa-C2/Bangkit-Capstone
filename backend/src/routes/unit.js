const express = require("express");
const router = express.Router();
const UserController = require('../controller/unit.js');

router.get('/', UserController.getAllUnit);

router.get('/:unit_id', UserController.getDetailUnit);



module.exports = router;