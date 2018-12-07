import enum


class DonorRhEnum(enum.Enum):
    Positive = "Positive"
    Negative = "Negative"


class RequestStatusEnum(enum.Enum):
    Donation = "Donation"
    Processing = "Processing"
    Testing = "Testing"
    Distribution = "Distribution"
