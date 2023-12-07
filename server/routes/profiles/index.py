from flask import Blueprint, request

from controller.profiles.get import get_profiles, get_params_profile, get_one_profiles
from controller.profiles.post import post_profile
from controller.profiles.put import put_params_profile
from controller.profiles.delete import delete_params_profile

from wrapper.protect_route import protect_route

profiles_blueprint = Blueprint("profiles", __name__)
@profiles_blueprint.route("/", methods=["GET"])
@protect_route
def get_route():
    dict_query = request.args.to_dict()
    profile_id = dict_query.get('_id')
    if profile_id:
        return get_one_profiles(profile_id) #one query
    else:
        return get_profiles()
    
@profiles_blueprint.route("/", methods=["POST"])
@protect_route
def post_route():
    return post_profile()


profiles_params_blueprint = Blueprint("profiles_one", __name__)
@profiles_params_blueprint.route("/", methods=["GET"])
@protect_route
def get_params_route(id):
    return get_params_profile(id)

@profiles_params_blueprint.route("/", methods=["PUT", "PATCH"])
@protect_route
def put_params_route(id):
    return put_params_profile(id)

@profiles_params_blueprint.route("/", methods=["DELETE"])
@protect_route
def delete_params_route(id):
    return delete_params_profile(id)