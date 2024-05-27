const express = require("express");
const router = express.Router();
const UserController = require('../controller/users.js');

router.get('/', UserController.getAllUsers);

module.exports = router;