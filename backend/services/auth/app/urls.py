from django.urls import path


from .repositories.user_repository import UserRepository
from .repositories.login_type_repository import LoginTypeRepository
from .repositories.two_factor_repository import TwoFactorRepository

from .services.jwt_service import JWTService
from .services.http_client import HttpClient
from .services.sign_in_up_oauth42_service import SignInOAuth42Service
from .services.two_factor_service import TwoFactorService
from .services.email_service import EmailService

from .interfaces.usecase.base_sign_up_usecase import BaseSignUpUseCase
from .interfaces.usecase.base_sign_in_usecase import BaseSignInUseCase
from .use_cases.get_user_usecase import GetUserUseCase
from .use_cases.edit_user_usecase import EditUserUseCase
from .use_cases.delete_user_usecase import DeleteUserUseCase
from .use_cases.sign_in_usecase import SignInUseCase
from .use_cases.sign_up_usecase import SignUpUseCase
from .use_cases.get_access_token_42_usecase import GetAccessToken42UseCase
from .use_cases.validate_access_token_42_usecase import ValidateAccessToken42UseCase
from .use_cases.get_me_42_usecase import GetMe42UseCase
from .use_cases.send_2factor_code_usecase import Send2FactorCodeUseCase

from .use_cases.validate_2factor_code_usecase import Validate2FactorCodeUseCase
from .controllers.sign_in_controller import SignInController
from .controllers.sign_up_controller import SignUpController
from .controllers.user_controller import UserController
from .controllers.sign_in_oauth42_controller import SignInOAuth42Controller
from .controllers.validate_2factor_code_controller import Validate2FactorCodeController

from .views import SignInView
from .views import SignUpView
from .views import UserView
from .views import GetUserView
from .views import RedirectOAuth42View
from .views import SignInOAuth42View
from .views import Validate2FactorCodeView

# repositories
user_repository = UserRepository()
login_type_repository = LoginTypeRepository()
two_factor_repository = TwoFactorRepository()

# services
token_service = JWTService()
email_service = EmailService()
http_client = HttpClient()
two_factor_service = TwoFactorService(
    two_factor_repository=two_factor_repository, email_service=email_service
)

# use cases
sign_in_use_case = SignInUseCase(
    user_repository=user_repository,
    token_service=token_service,
    two_factor_service=two_factor_service,
)
base_sign_up_usecase = BaseSignUpUseCase(user_repository, login_type_repository)
base_sign_in_usecase = BaseSignInUseCase(
    token_service=token_service, two_factor_service=two_factor_service
)
sign_up_use_case = SignUpUseCase(
    user_repository, login_type_repository, two_factor_service, base_sign_in_usecase
)
get_user_usecase = GetUserUseCase(user_repository)
edit_user_usecase = EditUserUseCase(user_repository)
delete_user_usecase = DeleteUserUseCase(user_repository)
get_access_token_42_use_case = GetAccessToken42UseCase(http_client)
validate_access_token_42_use_case = ValidateAccessToken42UseCase(http_client)
get_me_42_use_case = GetMe42UseCase(http_client)
send_2factor_code_usecase = Send2FactorCodeUseCase(
    user_repository, base_sign_in_usecase
)
validate_2factor_code_usecase = Validate2FactorCodeUseCase(
    user_repository, two_factor_service, base_sign_in_usecase
)
# services
sign_in_oauth42_service = SignInOAuth42Service(
    user_repository,
    base_sign_up_usecase,
    base_sign_in_usecase,
)

# controllers
sign_up_controller = SignUpController(sign_up_use_case)
sign_in_controller = SignInController(sign_in_use_case)
user_controller = UserController(
    get_user_usecase=get_user_usecase,
    edit_user_usecase=edit_user_usecase,
    delete_user_usecase=delete_user_usecase,
)
sign_in_oauth42_controller = SignInOAuth42Controller(
    http_client=http_client,
    get_access_token_42_use_case=get_access_token_42_use_case,
    validate_access_token_42_use_case=validate_access_token_42_use_case,
    get_me_42_use_case=get_me_42_use_case,
    sign_in_oauth42_service=sign_in_oauth42_service,
)
validate_2factor_code_controller = Validate2FactorCodeController(
    send_2factor_code_usecase=send_2factor_code_usecase,
    validate_2factor_code_usecase=validate_2factor_code_usecase,
)

urlpatterns = [
    path("sign-in/", SignInView.as_view(sign_in_controller=sign_in_controller)),
    path("redirect-42", RedirectOAuth42View.as_view()),
    path("sign-up/", SignUpView.as_view(sign_up_controller=sign_up_controller)),
    path("user/", GetUserView.as_view(user_controller=user_controller)),
    path("user/<uuid:user_id>", UserView.as_view(user_controller=user_controller)),
    path(
        "sign-in-42/",
        SignInOAuth42View.as_view(
            sign_in_oauth42_controller=sign_in_oauth42_controller
        ),
    ),
    path(
        "validate-2factor-code/",
        Validate2FactorCodeView.as_view(
            validate_2factor_code_controller=validate_2factor_code_controller
        ),
    ),
]