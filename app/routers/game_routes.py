from fastapi import APIRouter

router = APIRouter()


@router.get("/{game_id}/moves")
async def get_moves(game_id: int):
    ...


@router.post("/{game_id}/moves")
async def make_move(game_id: int):
    ...


@router.get("/games")
async def get_all_games():
    ...


@router.get("/{game_id}")
async def get_game(game_id: int):
    ...

@router.put("/{game_id}")
async def update_game(game_id: int):
    ...


@router.delete("/{game_id}")
async def delete_game(game_id: int):
    ...
