from resume_builder_v1.database.db import Profile, ProfileDataBase


def test_create_profile():

    local_str_profileName = "Sharath"

    local_obj_profile = Profile()
    local_obj_db = ProfileDataBase()
    local_obj_db.create(local_str_profileName,local_obj_profile)

def test_crud_profile():

    local_str_profileName = "Sharath"

    local_obj_profile = Profile()
    local_obj_db = ProfileDataBase()
    local_obj_db.create(local_str_profileName,local_obj_profile)

    # Read and update

    local_obj_existingProfile = local_obj_db.read(local_str_profileName)
    local_obj_existingProfile.obj_profileInfo.str_fullName = "Sharath B S"

    local_obj_db.update(local_str_profileName, local_obj_existingProfile)

    # read and verify
    local_obj_existingProfile = local_obj_db.read(local_str_profileName)
    assert local_obj_existingProfile.obj_profileInfo.str_fullName == "Sharath B S"

    # delete the profile

    local_obj_db.delete(local_str_profileName)
