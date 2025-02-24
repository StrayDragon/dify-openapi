from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_parameters_response_200_annotation_reply import GetParametersResponse200AnnotationReply
    from ..models.get_parameters_response_200_file_upload import GetParametersResponse200FileUpload
    from ..models.get_parameters_response_200_retriever_resource import GetParametersResponse200RetrieverResource
    from ..models.get_parameters_response_200_speech_to_text import GetParametersResponse200SpeechToText
    from ..models.get_parameters_response_200_suggested_questions_after_answer import (
        GetParametersResponse200SuggestedQuestionsAfterAnswer,
    )
    from ..models.get_parameters_response_200_system_parameters import GetParametersResponse200SystemParameters
    from ..models.get_parameters_response_200_user_input_form_item import GetParametersResponse200UserInputFormItem


T = TypeVar("T", bound="GetParametersResponse200")


@_attrs_define
class GetParametersResponse200:
    """
    Attributes:
        opening_statement (Union[Unset, str]): 开场白
        suggested_questions (Union[Unset, list[str]]): 开场推荐问题列表
        suggested_questions_after_answer (Union[Unset, GetParametersResponse200SuggestedQuestionsAfterAnswer]):
            回答后推荐问题设置
        speech_to_text (Union[Unset, GetParametersResponse200SpeechToText]): 语音转文本设置
        retriever_resource (Union[Unset, GetParametersResponse200RetrieverResource]): 引用和归属设置
        annotation_reply (Union[Unset, GetParametersResponse200AnnotationReply]): 标记回复设置
        user_input_form (Union[Unset, list['GetParametersResponse200UserInputFormItem']]): 用户输入表单配置
        file_upload (Union[Unset, GetParametersResponse200FileUpload]): 文件上传配置
        system_parameters (Union[Unset, GetParametersResponse200SystemParameters]): 系统参数
    """

    opening_statement: Union[Unset, str] = UNSET
    suggested_questions: Union[Unset, list[str]] = UNSET
    suggested_questions_after_answer: Union[Unset, "GetParametersResponse200SuggestedQuestionsAfterAnswer"] = UNSET
    speech_to_text: Union[Unset, "GetParametersResponse200SpeechToText"] = UNSET
    retriever_resource: Union[Unset, "GetParametersResponse200RetrieverResource"] = UNSET
    annotation_reply: Union[Unset, "GetParametersResponse200AnnotationReply"] = UNSET
    user_input_form: Union[Unset, list["GetParametersResponse200UserInputFormItem"]] = UNSET
    file_upload: Union[Unset, "GetParametersResponse200FileUpload"] = UNSET
    system_parameters: Union[Unset, "GetParametersResponse200SystemParameters"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        opening_statement = self.opening_statement

        suggested_questions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.suggested_questions, Unset):
            suggested_questions = self.suggested_questions

        suggested_questions_after_answer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.suggested_questions_after_answer, Unset):
            suggested_questions_after_answer = self.suggested_questions_after_answer.to_dict()

        speech_to_text: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.speech_to_text, Unset):
            speech_to_text = self.speech_to_text.to_dict()

        retriever_resource: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.retriever_resource, Unset):
            retriever_resource = self.retriever_resource.to_dict()

        annotation_reply: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.annotation_reply, Unset):
            annotation_reply = self.annotation_reply.to_dict()

        user_input_form: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.user_input_form, Unset):
            user_input_form = []
            for user_input_form_item_data in self.user_input_form:
                user_input_form_item = user_input_form_item_data.to_dict()
                user_input_form.append(user_input_form_item)

        file_upload: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.file_upload, Unset):
            file_upload = self.file_upload.to_dict()

        system_parameters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.system_parameters, Unset):
            system_parameters = self.system_parameters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if opening_statement is not UNSET:
            field_dict["opening_statement"] = opening_statement
        if suggested_questions is not UNSET:
            field_dict["suggested_questions"] = suggested_questions
        if suggested_questions_after_answer is not UNSET:
            field_dict["suggested_questions_after_answer"] = suggested_questions_after_answer
        if speech_to_text is not UNSET:
            field_dict["speech_to_text"] = speech_to_text
        if retriever_resource is not UNSET:
            field_dict["retriever_resource"] = retriever_resource
        if annotation_reply is not UNSET:
            field_dict["annotation_reply"] = annotation_reply
        if user_input_form is not UNSET:
            field_dict["user_input_form"] = user_input_form
        if file_upload is not UNSET:
            field_dict["file_upload"] = file_upload
        if system_parameters is not UNSET:
            field_dict["system_parameters"] = system_parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.get_parameters_response_200_annotation_reply import GetParametersResponse200AnnotationReply
        from ..models.get_parameters_response_200_file_upload import GetParametersResponse200FileUpload
        from ..models.get_parameters_response_200_retriever_resource import GetParametersResponse200RetrieverResource
        from ..models.get_parameters_response_200_speech_to_text import GetParametersResponse200SpeechToText
        from ..models.get_parameters_response_200_suggested_questions_after_answer import (
            GetParametersResponse200SuggestedQuestionsAfterAnswer,
        )
        from ..models.get_parameters_response_200_system_parameters import GetParametersResponse200SystemParameters
        from ..models.get_parameters_response_200_user_input_form_item import GetParametersResponse200UserInputFormItem

        d = src_dict.copy()
        opening_statement = d.pop("opening_statement", UNSET)

        suggested_questions = cast(list[str], d.pop("suggested_questions", UNSET))

        _suggested_questions_after_answer = d.pop("suggested_questions_after_answer", UNSET)
        suggested_questions_after_answer: Union[Unset, GetParametersResponse200SuggestedQuestionsAfterAnswer]
        if isinstance(_suggested_questions_after_answer, Unset):
            suggested_questions_after_answer = UNSET
        else:
            suggested_questions_after_answer = GetParametersResponse200SuggestedQuestionsAfterAnswer.from_dict(
                _suggested_questions_after_answer
            )

        _speech_to_text = d.pop("speech_to_text", UNSET)
        speech_to_text: Union[Unset, GetParametersResponse200SpeechToText]
        if isinstance(_speech_to_text, Unset):
            speech_to_text = UNSET
        else:
            speech_to_text = GetParametersResponse200SpeechToText.from_dict(_speech_to_text)

        _retriever_resource = d.pop("retriever_resource", UNSET)
        retriever_resource: Union[Unset, GetParametersResponse200RetrieverResource]
        if isinstance(_retriever_resource, Unset):
            retriever_resource = UNSET
        else:
            retriever_resource = GetParametersResponse200RetrieverResource.from_dict(_retriever_resource)

        _annotation_reply = d.pop("annotation_reply", UNSET)
        annotation_reply: Union[Unset, GetParametersResponse200AnnotationReply]
        if isinstance(_annotation_reply, Unset):
            annotation_reply = UNSET
        else:
            annotation_reply = GetParametersResponse200AnnotationReply.from_dict(_annotation_reply)

        user_input_form = []
        _user_input_form = d.pop("user_input_form", UNSET)
        for user_input_form_item_data in _user_input_form or []:
            user_input_form_item = GetParametersResponse200UserInputFormItem.from_dict(user_input_form_item_data)

            user_input_form.append(user_input_form_item)

        _file_upload = d.pop("file_upload", UNSET)
        file_upload: Union[Unset, GetParametersResponse200FileUpload]
        if isinstance(_file_upload, Unset):
            file_upload = UNSET
        else:
            file_upload = GetParametersResponse200FileUpload.from_dict(_file_upload)

        _system_parameters = d.pop("system_parameters", UNSET)
        system_parameters: Union[Unset, GetParametersResponse200SystemParameters]
        if isinstance(_system_parameters, Unset):
            system_parameters = UNSET
        else:
            system_parameters = GetParametersResponse200SystemParameters.from_dict(_system_parameters)

        get_parameters_response_200 = cls(
            opening_statement=opening_statement,
            suggested_questions=suggested_questions,
            suggested_questions_after_answer=suggested_questions_after_answer,
            speech_to_text=speech_to_text,
            retriever_resource=retriever_resource,
            annotation_reply=annotation_reply,
            user_input_form=user_input_form,
            file_upload=file_upload,
            system_parameters=system_parameters,
        )

        get_parameters_response_200.additional_properties = d
        return get_parameters_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
