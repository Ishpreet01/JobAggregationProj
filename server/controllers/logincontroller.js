const User = require('../models/User.js'); 

const loginUser = async(req,res) => {
     let user = await User.findOne({email: req.body.email});
     if(!user){
         return res.status(400).json({msg:"Email does not exist"});
     } else{
         return res.status(200).json({msg:"login successful", email: user.email, password: user.password});
     }
}


 module.exports = loginUser;