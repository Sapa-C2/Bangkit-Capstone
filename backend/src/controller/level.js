const UserModel = require('../model/level');

const getAllLevel = async(req, res) => {
    try {
        const [data]= await UserModel.getAllLevel();
        res.json({
          message: 'Get All level succees',
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
        if (!data) {
            return res.status(404).json({
                message: 'Level not found',
                serverMessage: `Level ID ${level_id} not found`
            });
        }
        const [unitsData] = await UserModel.getUnitsByLevelId(level_id);

        const result = {
            message: 'Get Detail level success',
            data: {
                data,
                unitsData,
            }
        };
        res.json(result);
    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({
            message: 'Server Error',
            serverMessage: error.message,
        });
    }
};




module.exports = {
    getAllLevel,
    getDetailLevel,
};
