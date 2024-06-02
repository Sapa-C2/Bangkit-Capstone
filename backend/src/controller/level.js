const UserModel = require('../model/level');

const getAllLevel = async(req, res) => {
    try {
        const [data]= await UserModel.getAllLevel();
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

const getDetailLevel = async (req, res) => {
    const { level_id } = req.params;
    try {
        const [data] = await UserModel.getDetailLevel(level_id);
        if (data.length === 0) {
            return res.status(404).json({
                message: 'not found',
                serverMessage: `Level  ID ${level_id} tidak ditemukan`
            });
        }
        res.json({
            message: 'Get Detail level success',
            data: data
        });
    } catch (error) {
        res.status(500).json({
            message: 'Server Error',
            serverMessage: error,
        });
    }
};

module.exports = {
    getAllLevel,
    getDetailLevel,
};
