from mgz.summary import Summary


def get_commands() -> dict:
    return {
        # META
        "completed": Summary.get_completed,
        "dataset": Summary.get_dataset,
        "encoding": Summary.get_encoding,
        "file_hash": Summary.get_file_hash,
        "hash": Summary.get_hash,
        "language": Summary.get_language,
        "mirror": Summary.get_mirror,
        "owner": Summary.get_owner,
        "platform": Summary.get_platform,
        "restored": get_restored,
        "version": get_version,

        # PLAYERS
        "chat": Summary.get_chat,
        "diplomacy": Summary.get_diplomacy,
        "players": Summary.get_players,
        "profiles": Summary.get_profile_ids,
        "ratings": Summary.get_ratings,
        "teams": Summary.get_teams,
        "achievements": Summary.has_achievements,

        # GAME
        "duration": Summary.get_duration,
        "map": Summary.get_map,
        "objects": Summary.get_objects,
        "postgame": Summary.get_postgame,
        "settings": Summary.get_settings,
        "start_time": Summary.get_start_time,
    }


def get_restored(summary: Summary) -> dict:
    return {
        "is_restored": summary.get_restored()[0],
        "time": summary.get_restored()[1],
    }


def get_version(summary: Summary) -> dict:
    return {
        "recanalyst": summary.get_version()[0],
        "game": summary.get_version()[1],
        "save": summary.get_version()[2],
        "log": summary.get_version()[3],
    }
