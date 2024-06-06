const UserModel = require('../model/unit');

const getAllUnit = async(req, res) => {
    try {
        const [data]= await UserModel.getAllUnit();
        res.json({
          message: 'Get All unit succees',
          data: data
        })
    } catch (error) {
        res.status(500).json({
            message: 'Server Error',
            serverMessage: error,
        })
    }
 
}

const getDetailUnit = async (req, res) => {
    const { unit_id } = req.params;
    try {
        const [data] = await UserModel.getDetailUnit(unit_id);
        if (data.length === 0) {
            return res.status(404).json({
                message: 'not found',
                serverMessage: `Unit  ID ${unit_id} tidak ditemukan`
            });
        }
        res.json({
            message: 'Get Detail unit success',
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
    getAllUnit,
    getDetailUnit,
}