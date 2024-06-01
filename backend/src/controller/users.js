const UserModel = require('../model/user');

const getAllUsers = async(req, res) => {
    try {
        const [data]= await UserModel.getAllUsers();
        res.json({
          message: 'Get All users succees',
          data: data
        })
    } catch (error) {
        res.status(500).json({
            message: 'Server Error',
            serverMessage: error,
        })
    }
 
}

const createNewUser = async(req, res) => {
    const {body} = req;

    if (!body.name || !body.password || !body.email) {
        return req.status(400).json ({
            message: 'Anda mengirimkan data yang salah',
            data: null
        })
    }
    try {
        await UserModel.createNewUser(body);
        res.status(201).json ({
            message: 'CREATE new users success',
            data: req.body
        })
    } catch (error) {
        res.status(500).json({
            message: 'Server Error',
            ServerMessage: error,
        })
    }
    
};

const UpdateUser = async(req, res) => {
    const {idUser} = req.params;
    const {body} = req;
    try {
        await UserModel.UpdateUser(body, idUser);
        res.json ({
            message: 'UPDATE user success',
            data: {
                id: idUser,
                ...body
            },
        })
        
    } catch (error) {
        res.status(500).json({
            message: 'Server Error',
            ServerMessage: error,
        })
    }
}

const DeleteUser = async(req, res) => {
    const {idUser} = req.params;
    try {
        await UserModel.DeleteUser(idUser);
        res.json ({
            message: 'Delete user success',
            data: null
        })

    } catch (error) {
        res.status(500).json({
            message: 'Server Error',
            ServerMessage: error,
        })
    }
}

module.exports = {
    getAllUsers,
    createNewUser,
    UpdateUser,
    DeleteUser,
};