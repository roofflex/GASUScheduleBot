from loader import dp
from .admin_filter import IsAdmin
from .user_filter import IsUser


if __name__ == "filters":
     dp.filters_factory.bind(IsAdmin)
     dp.filters_factory.bind(IsUser)

