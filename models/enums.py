from enum import Enum


class StrEnum(str, Enum):
    def __str__(self):
        return self.value


class Schema(StrEnum):
    sample_product = "sample_product"
    user = "user"
    user_otp = "user_otp"


class Space(StrEnum):
    acme = "acme"


class Status(StrEnum):
    success = "success"
    failed = "failed"


class OperatingSystems(StrEnum):
    android = "android"
    ios = "ios"


class Language(StrEnum):
    ar = "ar"
    en = "en"
    kd = "kd"


class OTPFor(StrEnum):
    mail_verification = "mail_verification"
    phone_verification = "phone_verification"
    reset_password = "reset_password"
