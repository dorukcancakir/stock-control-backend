import strawberry as sb
import strawberry_django as sb_django
import core.models as models


def description(string):
    return sb.field(description=string)


def resolve(string):
    def resolver(root):
        attribute = getattr(root, string)
        try:
            return getattr(attribute, 'url')
        except (AttributeError, ValueError):
            return attribute

    return sb.field(resolver=resolver)


@sb.type
class SuccessResponse:
    success: bool


@sb_django.type(models.Company)
class CompanyType:
    id: sb.auto
    name: sb.auto
    created_at: sb.auto


@sb_django.type(models.User)
class UserType:
    id: sb.auto
    company: CompanyType
    email: sb.auto
    first_name: sb.auto
    last_name: sb.auto
    role: sb.auto
    created_at: sb.auto
    updated_at: sb.auto


@sb_django.type(models.ItemCategory)
class ItemCategoryType:
    id: sb.auto
    company: CompanyType
    name: sb.auto
    created_at: sb.auto
    updated_at: sb.auto


@sb_django.type(models.Item)
class ItemType:
    id: sb.auto
    company: CompanyType
    category: ItemCategoryType
    name: sb.auto
    quantity: sb.auto
    min_quantity: sb.auto
    image: sb.auto
    unit_of_measurement: sb.auto
