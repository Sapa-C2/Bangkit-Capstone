
const getAllUsers = (req, res) => {
    res.json({
        message: 'Get All User Success',
    })
}

const createNewUser = (req, res) => {
    console.log(req.body);
    res.json({
        message: 'Create new user success',
        data: req.body
    })
}

const UpdateUser = (req, res) => {
    const {idUser} = req.params;
    res.json({
        message: 'Update user success',
        data: req.body
    })
}

const DeleteUser = (req, res) => {
    const {idUser} = req.params;
    res.json({
        message: 'Delete user success',
        data: {
            id: idUser,
            name: "iyas"
        }
    })
}

module.exports = {
    getAllUsers,
    createNewUser,
    UpdateUser,
    DeleteUser,
};