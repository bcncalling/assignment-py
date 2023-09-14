from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse
from ..db.connection import collection
from ..db.model import User
from bson import ObjectId
from io import BytesIO

app = FastAPI()

# Create, Read, Update, Delete (CRUD) operations
@app.post("/user")
async def create_user(user : User):
    try :
        user = dict(user)
        await collection.insert_one(user)
        return JSONResponse(status_code=200, content={"message": "User created successfully"})
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"message": "Could not create user"})
    
@app.get("/users")
async def get_users():
    try :
        users = []
        async for user in collection.find():
            user['_id'] = str(user['_id'])
            if 'profile_pic' in user:
                del user['profile_pic']['data']
                
            users.append(user)

        return JSONResponse(status_code=200, content={"users": users})
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"message": "Could not fetch users"})
    
@app.get("/user/{id}")
async def get_user(id : str):
    try :
        user = await collection.find_one({"_id": ObjectId(id)})
        user['_id'] = str(user['_id'])
        if 'profile_pic' in user:
            del user['profile_pic']['data']
        return JSONResponse(status_code=200, content={"user": user})
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"message": "Could not fetch user"})
    
@app.put("/user/{id}")
async def update_user(id : str, user : User):
    try :
        user_exists = await collection.find_one({"_id": ObjectId(id)})
        if not user_exists:
            return JSONResponse(status_code=400, content={"message": "User does not exist"})
        await collection.update_one({"_id": ObjectId(id)}, {"$set": dict(user)})
        return JSONResponse(status_code=200, content={"message": "User updated successfully"})
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"message": "Could not update user"})
    
@app.delete("/user/{id}")
async def delete_user(id : str):
    try :
        user_exists = await collection.find_one({"_id": ObjectId(id)})
        if not user_exists:
            return JSONResponse(status_code=400, content={"message": "User does not exist"})
        await collection.delete_one({"_id": ObjectId(id)})
        return JSONResponse(status_code=200, content={"message": "User deleted successfully"})
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"message": "Could not delete user"})

# Upload and download profile pic
@app.post("/upload_profile_pic/{id}")
async def upload_profile_pic(id : str,file : UploadFile = File(...)):
    try :
        user_exists = await collection.find_one({"_id": ObjectId(id)})
        if not user_exists:
            return JSONResponse(status_code=400, content={"message": "User does not exist"})
        contents = await file.read()
        profile_pic = {"filename": file.filename, "data": contents}
        await collection.update_one({"_id": ObjectId(id)}, {"$set": {"profile_pic": profile_pic}})
        return JSONResponse(status_code=200, content={"message": "Profile pic uploaded successfully"})
    except Exception as e:
        print(e) 
        return JSONResponse(status_code=500, content={"message": "Could not upload profile pic"})
    
@app.get("/get_profile_pic/{id}")
async def get_profile_pic(id : str):
    try :
        user = await collection.find_one({"_id": ObjectId(id)})
        if not user:
            return JSONResponse(status_code=400, content={"message": "User does not exist"})
        return StreamingResponse(BytesIO(user['profile_pic']['data']), media_type='image/png', headers={"Content-Disposition": f'attachment; filename="{user["profile_pic"]["filename"]}"'})
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"message": "Could not fetch profile pic"})
        

        
        
