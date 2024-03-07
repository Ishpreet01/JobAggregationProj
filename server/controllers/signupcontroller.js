const User = require('../models/User.js'); 

const signupUser = async (req,res) =>{
     try{
          const user = req.body;
          const newUser = new User(user); //validated object
          await newUser.save();

          return res.status(200).json({msg:'signup successful',name:user.name,phone:user.phone,password:user.password,username:user.username,email:user.email,qual:user.qual});
     } catch(error){
        
        return res.status(500).json({msg:'Error while signup'});
     }
}




 module.exports = signupUser;


//here each subsequent line overrides the other so only the loginUser is being exported
// module.exports = signupUser;
// module.exports = loginUser;