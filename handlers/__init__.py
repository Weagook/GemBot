from .start import router as start_router
from .get_name import router as get_name_router
from .callbacks import router as callback_router
from .images_id import router as image_router


def setup_routers(dp):
    dp.include_router(start_router)
    dp.include_router(get_name_router)
    dp.include_router(callback_router)
    dp.include_router(image_router)