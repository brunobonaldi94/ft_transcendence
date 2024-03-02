
from ..dtos.user_edit_dto import UserEditDto, UserEditDtoForm
from ..interfaces.controllers.base_controller import BaseController
from django.http import HttpRequest, JsonResponse
from ..interfaces.usecase.base_usecase import BaseUseCase

class UserController(BaseController):

  def __init__(self, edit_user_usecase: BaseUseCase, delete_user_usecase: BaseUseCase) -> None:
    super().__init__()
    self.edit_user_usecase = edit_user_usecase
    self.delete_user_usecase = delete_user_usecase

  def convert_to_form(self, request: HttpRequest) -> dict:
    user_edit_form = UserEditDtoForm(request.POST)
    print(user_edit_form)
    return user_edit_form
  def convert_to_dto(self, data: dict) -> UserEditDto:
    return UserEditDto(user_name=data.get('user_name'), email=data.get('email'), enable_2fa=data.get('enable_2fa'), password=data.get('password'))

  async def execute_put(self, user_id: str, dto: UserEditDto) -> JsonResponse:
   return await self.edit_user_usecase.execute(user_id, dto)