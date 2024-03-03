const User = require('../models/User.js'); 

 const signupUser = async (req,res) =>{
     try{
          const user = req.body;
          const newUser = new User(user); //validated object
          await newUser.save();

          return res.status(200).json({msg:'signup successful'});
     } catch(error){
         return res.status(500).json({msg:'Error while signup'});
     }
}

const loginUser = async(req,res) => {
     let user = await User.findOne({username: req.body.email});
     if(!user){
         return res.status(400).json({msg:"Email does not exist"});
     } else{
         return res.status(200).json({msg:"login successful"});
     }
}

module.exports = signupUser;
module.exports = loginUser;