const User = require('../models/User.js'); 

const loginUser = async(req,res) => {
     let user = await User.findOne({username: req.body.email});
     if(!user){
         return res.status(400).json({msg:"Email does not exist"});
     } else{
         return res.status(200).json({msg:"login successful"});
     }
}


 module.exports = loginUser;