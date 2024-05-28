const express = require("express");
const router = express.Router();
const UserController = require('../controller/users.js');

router.get('/', UserController.getAllUsers);

router.post('/', UserController.createNewUser);

router.patch('/:idUser', UserController.UpdateUser);

router.delete('/:idUser', UserController.DeleteUser);

module.exports = router;