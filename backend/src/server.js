require('dotenv').config();

const express = require("express");

const app = express();
const usersRoutes = require('./routes/users.js');
const levelRoutes = require('./routes/level.js');
const MiddlewareLogsrequest = require('./middleware/logs.js');


app.use(MiddlewareLogsrequest);
app.use(express.json());

app.use('/users', usersRoutes);
//app.use('/level', levelRoutes);
//app.use('/unit', unitRoutes);


app.get("/", (req, res) => {
    res.send("hello")
});


app.listen(4000, () => {
    console.log('Server berhasil di running di port 4000');
})
