const StageModel = require("../model/stage.js"); // Adjust the path as necessary

const getAllStages = async (req, res) => {
  try {
    const [data] = await StageModel.getAllStage();
    res.json({
      message: "Get All Stages Success",
      data: data,
    });
  } catch (error) {
    res.status(500).json({
      message: "Server Error",
      serverMessage: error.message,
    });
  }
};

const getDetailStage = async (req, res) => {
  const { stage_id } = req.params;

  try {
    const [data] = await StageModel.getDetailStage(stage_id);
    if (!data.length) {
      // Adjusted to check for an empty array
      return res.status(404).json({
        message: "Stage not found",
        serverMessage: `Stage ID ${stage_id} not found`,
      });
    }
    const [questionsData] = await StageModel.getQuestionsByStageId(stage_id);
    const result = {
      message: "Get Detail Stage Success",
      data: {
        stage: data[0],
        questions: questionsData,
      },
    };
    res.json(result);
  } catch (error) {
    console.error("Error:", error);
    res.status(500).json({
      message: "Server Error",
      serverMessage: error.message,
    });
  }
};

module.exports = {
  getAllStages,
  getDetailStage,
};
