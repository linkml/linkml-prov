# Auto generated from prov.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-09-02 19:35
# Schema: prov
#
# id: http://www.w3.org/ns/prov#
# description: prov
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LINKML_PROV = CurieNamespace('linkml_prov', 'https://w3id.org/linkml/prov/')
OWL = CurieNamespace('owl', 'http://example.org/UNKNOWN/owl/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
DEFAULT_ = LINKML_PROV


# Types

# Class references



class Thing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Thing
    class_class_curie: ClassVar[str] = "owl:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Thing


@dataclass
class Activity(YAMLRoot):
    """
    An activity is something that occurs over a period of time and acts upon or with entities; it may include
    consuming, processing, transforming, modifying, relocating, using, or generating entities.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Activity
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Activity

    atLocation: Optional[Union[dict, "Location"]] = None
    generated: Optional[Union[dict, "Entity"]] = None
    invalidated: Optional[Union[dict, "Entity"]] = None
    qualifiedAssociation: Optional[Union[dict, "Association"]] = None
    qualifiedCommunication: Optional[Union[dict, "Communication"]] = None
    qualifiedEnd: Optional[Union[dict, "End"]] = None
    qualifiedInfluence: Optional[Union[dict, "Influence"]] = None
    qualifiedStart: Optional[Union[dict, "Start"]] = None
    qualifiedUsage: Optional[Union[dict, "Usage"]] = None
    used: Optional[Union[dict, "Entity"]] = None
    wasAssociatedWith: Optional[Union[dict, "Agent"]] = None
    wasEndedBy: Optional[Union[dict, "Entity"]] = None
    wasInfluencedBy: Optional[str] = None
    wasInformedBy: Optional[Union[dict, "Activity"]] = None
    wasStartedBy: Optional[Union[dict, "Entity"]] = None
    endedAtTime: Optional[str] = None
    startedAtTime: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.atLocation is not None and not isinstance(self.atLocation, Location):
            self.atLocation = Location()

        if self.generated is not None and not isinstance(self.generated, Entity):
            self.generated = Entity(**self.generated)

        if self.invalidated is not None and not isinstance(self.invalidated, Entity):
            self.invalidated = Entity(**self.invalidated)

        if self.qualifiedAssociation is not None and not isinstance(self.qualifiedAssociation, Association):
            self.qualifiedAssociation = Association(**self.qualifiedAssociation)

        if self.qualifiedCommunication is not None and not isinstance(self.qualifiedCommunication, Communication):
            self.qualifiedCommunication = Communication(**self.qualifiedCommunication)

        if self.qualifiedEnd is not None and not isinstance(self.qualifiedEnd, End):
            self.qualifiedEnd = End(**self.qualifiedEnd)

        if self.qualifiedInfluence is not None and not isinstance(self.qualifiedInfluence, Influence):
            self.qualifiedInfluence = Influence(**self.qualifiedInfluence)

        if self.qualifiedStart is not None and not isinstance(self.qualifiedStart, Start):
            self.qualifiedStart = Start(**self.qualifiedStart)

        if self.qualifiedUsage is not None and not isinstance(self.qualifiedUsage, Usage):
            self.qualifiedUsage = Usage(**self.qualifiedUsage)

        if self.used is not None and not isinstance(self.used, Entity):
            self.used = Entity(**self.used)

        if self.wasAssociatedWith is not None and not isinstance(self.wasAssociatedWith, Agent):
            self.wasAssociatedWith = Agent(**self.wasAssociatedWith)

        if self.wasEndedBy is not None and not isinstance(self.wasEndedBy, Entity):
            self.wasEndedBy = Entity(**self.wasEndedBy)

        if self.wasInfluencedBy is not None and not isinstance(self.wasInfluencedBy, str):
            self.wasInfluencedBy = str(self.wasInfluencedBy)

        if self.wasInformedBy is not None and not isinstance(self.wasInformedBy, Activity):
            self.wasInformedBy = Activity(**self.wasInformedBy)

        if self.wasStartedBy is not None and not isinstance(self.wasStartedBy, Entity):
            self.wasStartedBy = Entity(**self.wasStartedBy)

        if self.endedAtTime is not None and not isinstance(self.endedAtTime, str):
            self.endedAtTime = str(self.endedAtTime)

        if self.startedAtTime is not None and not isinstance(self.startedAtTime, str):
            self.startedAtTime = str(self.startedAtTime)

        super().__post_init__(**kwargs)


@dataclass
class Agent(YAMLRoot):
    """
    An agent is something that bears some form of responsibility for an activity taking place, for the existence of an
    entity, or for another agent's activity. @en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Agent
    class_class_curie: ClassVar[str] = "prov:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Agent

    actedOnBehalfOf: Optional[Union[dict, "Agent"]] = None
    atLocation: Optional[Union[dict, "Location"]] = None
    qualifiedDelegation: Optional[Union[dict, "Delegation"]] = None
    qualifiedInfluence: Optional[Union[dict, "Influence"]] = None
    wasInfluencedBy: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.actedOnBehalfOf is not None and not isinstance(self.actedOnBehalfOf, Agent):
            self.actedOnBehalfOf = Agent(**self.actedOnBehalfOf)

        if self.atLocation is not None and not isinstance(self.atLocation, Location):
            self.atLocation = Location()

        if self.qualifiedDelegation is not None and not isinstance(self.qualifiedDelegation, Delegation):
            self.qualifiedDelegation = Delegation(**self.qualifiedDelegation)

        if self.qualifiedInfluence is not None and not isinstance(self.qualifiedInfluence, Influence):
            self.qualifiedInfluence = Influence(**self.qualifiedInfluence)

        if self.wasInfluencedBy is not None and not isinstance(self.wasInfluencedBy, str):
            self.wasInfluencedBy = str(self.wasInfluencedBy)

        super().__post_init__(**kwargs)


@dataclass
class Entity(YAMLRoot):
    """
    An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real
    or imaginary. @en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Entity
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Entity

    alternateOf: Optional[Union[dict, "Entity"]] = None
    atLocation: Optional[Union[dict, "Location"]] = None
    hadPrimarySource: Optional[Union[dict, "Entity"]] = None
    qualifiedAttribution: Optional[Union[dict, Attribution]] = None
    qualifiedDerivation: Optional[Union[dict, Derivation]] = None
    qualifiedGeneration: Optional[Union[dict, "Generation"]] = None
    qualifiedInfluence: Optional[Union[dict, "Influence"]] = None
    qualifiedInvalidation: Optional[Union[dict, "Invalidation"]] = None
    qualifiedPrimarySource: Optional[Union[dict, "PrimarySource"]] = None
    qualifiedQuotation: Optional[Union[dict, "Quotation"]] = None
    qualifiedRevision: Optional[Union[dict, "Revision"]] = None
    specializationOf: Optional[Union[dict, "Entity"]] = None
    wasAttributedTo: Optional[Union[dict, Agent]] = None
    wasDerivedFrom: Optional[Union[dict, "Entity"]] = None
    wasGeneratedBy: Optional[Union[dict, Activity]] = None
    wasInfluencedBy: Optional[str] = None
    wasInvalidatedBy: Optional[Union[dict, Activity]] = None
    wasQuotedFrom: Optional[Union[dict, "Entity"]] = None
    wasRevisionOf: Optional[Union[dict, "Entity"]] = None
    generatedAtTime: Optional[str] = None
    invalidatedAtTime: Optional[str] = None
    value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.alternateOf is not None and not isinstance(self.alternateOf, Entity):
            self.alternateOf = Entity(**self.alternateOf)

        if self.atLocation is not None and not isinstance(self.atLocation, Location):
            self.atLocation = Location()

        if self.hadPrimarySource is not None and not isinstance(self.hadPrimarySource, Entity):
            self.hadPrimarySource = Entity(**self.hadPrimarySource)

        if self.qualifiedAttribution is not None and not isinstance(self.qualifiedAttribution, Attribution):
            self.qualifiedAttribution = Attribution(**self.qualifiedAttribution)

        if self.qualifiedDerivation is not None and not isinstance(self.qualifiedDerivation, Derivation):
            self.qualifiedDerivation = Derivation(**self.qualifiedDerivation)

        if self.qualifiedGeneration is not None and not isinstance(self.qualifiedGeneration, Generation):
            self.qualifiedGeneration = Generation(**self.qualifiedGeneration)

        if self.qualifiedInfluence is not None and not isinstance(self.qualifiedInfluence, Influence):
            self.qualifiedInfluence = Influence(**self.qualifiedInfluence)

        if self.qualifiedInvalidation is not None and not isinstance(self.qualifiedInvalidation, Invalidation):
            self.qualifiedInvalidation = Invalidation(**self.qualifiedInvalidation)

        if self.qualifiedPrimarySource is not None and not isinstance(self.qualifiedPrimarySource, PrimarySource):
            self.qualifiedPrimarySource = PrimarySource(**self.qualifiedPrimarySource)

        if self.qualifiedQuotation is not None and not isinstance(self.qualifiedQuotation, Quotation):
            self.qualifiedQuotation = Quotation(**self.qualifiedQuotation)

        if self.qualifiedRevision is not None and not isinstance(self.qualifiedRevision, Revision):
            self.qualifiedRevision = Revision(**self.qualifiedRevision)

        if self.specializationOf is not None and not isinstance(self.specializationOf, Entity):
            self.specializationOf = Entity(**self.specializationOf)

        if self.wasAttributedTo is not None and not isinstance(self.wasAttributedTo, Agent):
            self.wasAttributedTo = Agent(**self.wasAttributedTo)

        if self.wasDerivedFrom is not None and not isinstance(self.wasDerivedFrom, Entity):
            self.wasDerivedFrom = Entity(**self.wasDerivedFrom)

        if self.wasGeneratedBy is not None and not isinstance(self.wasGeneratedBy, Activity):
            self.wasGeneratedBy = Activity(**self.wasGeneratedBy)

        if self.wasInfluencedBy is not None and not isinstance(self.wasInfluencedBy, str):
            self.wasInfluencedBy = str(self.wasInfluencedBy)

        if self.wasInvalidatedBy is not None and not isinstance(self.wasInvalidatedBy, Activity):
            self.wasInvalidatedBy = Activity(**self.wasInvalidatedBy)

        if self.wasQuotedFrom is not None and not isinstance(self.wasQuotedFrom, Entity):
            self.wasQuotedFrom = Entity(**self.wasQuotedFrom)

        if self.wasRevisionOf is not None and not isinstance(self.wasRevisionOf, Entity):
            self.wasRevisionOf = Entity(**self.wasRevisionOf)

        if self.generatedAtTime is not None and not isinstance(self.generatedAtTime, str):
            self.generatedAtTime = str(self.generatedAtTime)

        if self.invalidatedAtTime is not None and not isinstance(self.invalidatedAtTime, str):
            self.invalidatedAtTime = str(self.invalidatedAtTime)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


class Bundle(Entity):
    """
    A bundle is a named set of provenance descriptions, and is itself an Entity, so allowing provenance of provenance
    to be expressed.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Bundle
    class_class_curie: ClassVar[str] = "prov:Bundle"
    class_name: ClassVar[str] = "Bundle"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Bundle


@dataclass
class Collection(Entity):
    """
    A collection is an entity that provides a structure to some constituents, which are themselves entities. These
    constituents are said to be member of the collections.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Collection
    class_class_curie: ClassVar[str] = "prov:Collection"
    class_name: ClassVar[str] = "Collection"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Collection

    hadMember: Optional[Union[dict, "Entity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hadMember is not None and not isinstance(self.hadMember, Entity):
            self.hadMember = Entity(**self.hadMember)

        super().__post_init__(**kwargs)


class EmptyCollection(Collection):
    """
    An empty collection is a collection without members.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.EmptyCollection
    class_class_curie: ClassVar[str] = "prov:EmptyCollection"
    class_name: ClassVar[str] = "EmptyCollection"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.EmptyCollection


@dataclass
class Influence(YAMLRoot):
    """
    Influence is the capacity of an entity, activity, or agent to have an effect on the character, development, or
    behavior of another by means of usage, start, end, generation, invalidation, communication, derivation,
    attribution, association, or delegation.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Influence
    class_class_curie: ClassVar[str] = "prov:Influence"
    class_name: ClassVar[str] = "Influence"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Influence

    hadActivity: Optional[Union[dict, Activity]] = None
    hadRole: Optional[Union[dict, "Role"]] = None
    influencer: Optional[Union[dict, Thing]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hadActivity is not None and not isinstance(self.hadActivity, Activity):
            self.hadActivity = Activity(**self.hadActivity)

        if self.hadRole is not None and not isinstance(self.hadRole, Role):
            self.hadRole = Role()

        if self.influencer is not None and not isinstance(self.influencer, Thing):
            self.influencer = Thing()

        super().__post_init__(**kwargs)


@dataclass
class ActivityInfluence(Influence):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.ActivityInfluence
    class_class_curie: ClassVar[str] = "prov:ActivityInfluence"
    class_name: ClassVar[str] = "ActivityInfluence"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.ActivityInfluence

    activity: Optional[Union[dict, Activity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.activity is not None and not isinstance(self.activity, Activity):
            self.activity = Activity(**self.activity)

        super().__post_init__(**kwargs)


@dataclass
class AgentInfluence(Influence):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.AgentInfluence
    class_class_curie: ClassVar[str] = "prov:AgentInfluence"
    class_name: ClassVar[str] = "AgentInfluence"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.AgentInfluence

    agent: Optional[Union[dict, Agent]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.agent is not None and not isinstance(self.agent, Agent):
            self.agent = Agent(**self.agent)

        super().__post_init__(**kwargs)


@dataclass
class Association(AgentInfluence):
    """
    An activity association is an assignment of responsibility to an agent for an activity, indicating that the agent
    had a role in the activity. It further allows for a plan to be specified, which is the plan intended by the agent
    to achieve some goals in the context of this activity.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Association
    class_class_curie: ClassVar[str] = "prov:Association"
    class_name: ClassVar[str] = "Association"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Association

    hadPlan: Optional[Union[dict, "Plan"]] = None
    hadRole: Optional[Union[dict, "Role"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hadPlan is not None and not isinstance(self.hadPlan, Plan):
            self.hadPlan = Plan(**self.hadPlan)

        if self.hadRole is not None and not isinstance(self.hadRole, Role):
            self.hadRole = Role()

        super().__post_init__(**kwargs)


class Attribution(AgentInfluence):
    """
    Attribution is the ascribing of an entity to an agent.

    When an entity e is attributed to agent ag, entity e was generated by some unspecified activity that in turn was
    associated to agent ag. Thus, this relation is useful when the activity is not known, or irrelevant.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Attribution
    class_class_curie: ClassVar[str] = "prov:Attribution"
    class_name: ClassVar[str] = "Attribution"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Attribution


class Communication(ActivityInfluence):
    """
    Communication is the exchange of an entity by two activities, one activity using the entity generated by the other.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Communication
    class_class_curie: ClassVar[str] = "prov:Communication"
    class_name: ClassVar[str] = "Communication"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Communication


@dataclass
class Delegation(AgentInfluence):
    """
    Delegation is the assignment of authority and responsibility to an agent (by itself or by another agent) to carry
    out a specific activity as a delegate or representative, while the agent it acts on behalf of retains some
    responsibility for the outcome of the delegated work.

    For example, a student acted on behalf of his supervisor, who acted on behalf of the department chair, who acted
    on behalf of the university; all those agents are responsible in some way for the activity that took place but we
    do not say explicitly who bears responsibility and to what degree.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Delegation
    class_class_curie: ClassVar[str] = "prov:Delegation"
    class_name: ClassVar[str] = "Delegation"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Delegation

    hadActivity: Optional[Union[dict, Activity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hadActivity is not None and not isinstance(self.hadActivity, Activity):
            self.hadActivity = Activity(**self.hadActivity)

        super().__post_init__(**kwargs)


@dataclass
class EntityInfluence(Influence):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.EntityInfluence
    class_class_curie: ClassVar[str] = "prov:EntityInfluence"
    class_name: ClassVar[str] = "EntityInfluence"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.EntityInfluence

    entity: Optional[Union[dict, Entity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.entity is not None and not isinstance(self.entity, Entity):
            self.entity = Entity(**self.entity)

        super().__post_init__(**kwargs)


@dataclass
class Derivation(EntityInfluence):
    """
    A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the
    construction of a new entity based on a pre-existing entity.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Derivation
    class_class_curie: ClassVar[str] = "prov:Derivation"
    class_name: ClassVar[str] = "Derivation"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Derivation

    hadActivity: Optional[Union[dict, Activity]] = None
    hadGeneration: Optional[Union[dict, "Generation"]] = None
    hadUsage: Optional[Union[dict, "Usage"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hadActivity is not None and not isinstance(self.hadActivity, Activity):
            self.hadActivity = Activity(**self.hadActivity)

        if self.hadGeneration is not None and not isinstance(self.hadGeneration, Generation):
            self.hadGeneration = Generation(**self.hadGeneration)

        if self.hadUsage is not None and not isinstance(self.hadUsage, Usage):
            self.hadUsage = Usage(**self.hadUsage)

        super().__post_init__(**kwargs)


@dataclass
class InstantaneousEvent(YAMLRoot):
    """
    The PROV data model is implicitly based on a notion of instantaneous events (or just events), that mark
    transitions in the world. Events include generation, usage, or invalidation of entities, as well as starting or
    ending of activities. This notion of event is not first-class in the data model, but it is useful for explaining
    its other concepts and its semantics.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.InstantaneousEvent
    class_class_curie: ClassVar[str] = "prov:InstantaneousEvent"
    class_name: ClassVar[str] = "InstantaneousEvent"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.InstantaneousEvent

    atLocation: Optional[Union[dict, "Location"]] = None
    hadRole: Optional[Union[dict, "Role"]] = None
    atTime: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.atLocation is not None and not isinstance(self.atLocation, Location):
            self.atLocation = Location()

        if self.hadRole is not None and not isinstance(self.hadRole, Role):
            self.hadRole = Role()

        if self.atTime is not None and not isinstance(self.atTime, str):
            self.atTime = str(self.atTime)

        super().__post_init__(**kwargs)


@dataclass
class End(InstantaneousEvent):
    """
    End is when an activity is deemed to have been ended by an entity, known as trigger. The activity no longer exists
    after its end. Any usage, generation, or invalidation involving an activity precedes the activity's end. An end
    may refer to a trigger entity that terminated the activity, or to an activity, known as ender that generated the
    trigger.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.End
    class_class_curie: ClassVar[str] = "prov:End"
    class_name: ClassVar[str] = "End"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.End

    hadActivity: Optional[Union[dict, Activity]] = None
    entity: Optional[Union[dict, "Entity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hadActivity is not None and not isinstance(self.hadActivity, Activity):
            self.hadActivity = Activity(**self.hadActivity)

        if self.entity is not None and not isinstance(self.entity, Entity):
            self.entity = Entity(**self.entity)

        super().__post_init__(**kwargs)


@dataclass
class Generation(InstantaneousEvent):
    """
    Generation is the completion of production of a new entity by an activity. This entity did not exist before
    generation and becomes available for usage after this generation.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Generation
    class_class_curie: ClassVar[str] = "prov:Generation"
    class_name: ClassVar[str] = "Generation"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Generation

    activity: Optional[Union[dict, Activity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.activity is not None and not isinstance(self.activity, Activity):
            self.activity = Activity(**self.activity)

        super().__post_init__(**kwargs)


@dataclass
class Invalidation(InstantaneousEvent):
    """
    Invalidation is the start of the destruction, cessation, or expiry of an existing entity by an activity. The
    entity is no longer available for use (or further invalidation) after invalidation. Any generation or usage of an
    entity precedes its invalidation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Invalidation
    class_class_curie: ClassVar[str] = "prov:Invalidation"
    class_name: ClassVar[str] = "Invalidation"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Invalidation

    activity: Optional[Union[dict, Activity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.activity is not None and not isinstance(self.activity, Activity):
            self.activity = Activity(**self.activity)

        super().__post_init__(**kwargs)


class Location(YAMLRoot):
    """
    A location can be an identifiable geographic place (ISO 19112), but it can also be a non-geographic place such as
    a directory, row, or column. As such, there are numerous ways in which location can be expressed, such as by a
    coordinate, address, landmark, and so forth.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Location
    class_class_curie: ClassVar[str] = "prov:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Location


class Organization(Agent):
    """
    An organization is a social or legal institution such as a company, society, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Organization
    class_class_curie: ClassVar[str] = "prov:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Organization


class Person(Agent):
    """
    Person agents are people.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Person
    class_class_curie: ClassVar[str] = "prov:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Person


class Plan(Entity):
    """
    A plan is an entity that represents a set of actions or steps intended by one or more agents to achieve some goals.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Plan
    class_class_curie: ClassVar[str] = "prov:Plan"
    class_name: ClassVar[str] = "Plan"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Plan


class PrimarySource(Derivation):
    """
    A primary source for a topic refers to something produced by some agent with direct experience and knowledge about
    the topic, at the time of the topic's study, without benefit from hindsight.

    Because of the directness of primary sources, they 'speak for themselves' in ways that cannot be captured through
    the filter of secondary sources. As such, it is important for secondary sources to reference those primary sources
    from which they were derived, so that their reliability can be investigated.

    A primary source relation is a particular case of derivation of secondary materials from their primary sources. It
    is recognized that the determination of primary sources can be up to interpretation, and should be done according
    to conventions accepted within the application's domain.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.PrimarySource
    class_class_curie: ClassVar[str] = "prov:PrimarySource"
    class_name: ClassVar[str] = "PrimarySource"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.PrimarySource


class Quotation(Derivation):
    """
    A quotation is the repeat of (some or all of) an entity, such as text or image, by someone who may or may not be
    its original author. Quotation is a particular case of derivation.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Quotation
    class_class_curie: ClassVar[str] = "prov:Quotation"
    class_name: ClassVar[str] = "Quotation"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Quotation


class Revision(Derivation):
    """
    A revision is a derivation for which the resulting entity is a revised version of some original. The implication
    here is that the resulting entity contains substantial content from the original. Revision is a particular case of
    derivation.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Revision
    class_class_curie: ClassVar[str] = "prov:Revision"
    class_name: ClassVar[str] = "Revision"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Revision


class Role(YAMLRoot):
    """
    A role is the function of an entity or agent with respect to an activity, in the context of a usage, generation,
    invalidation, association, start, and end.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Role
    class_class_curie: ClassVar[str] = "prov:Role"
    class_name: ClassVar[str] = "Role"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Role


class SoftwareAgent(Agent):
    """
    A software agent is running software.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.SoftwareAgent
    class_class_curie: ClassVar[str] = "prov:SoftwareAgent"
    class_name: ClassVar[str] = "SoftwareAgent"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.SoftwareAgent


@dataclass
class Start(InstantaneousEvent):
    """
    Start is when an activity is deemed to have been started by an entity, known as trigger. The activity did not
    exist before its start. Any usage, generation, or invalidation involving an activity follows the activity's start.
    A start may refer to a trigger entity that set off the activity, or to an activity, known as starter, that
    generated the trigger.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Start
    class_class_curie: ClassVar[str] = "prov:Start"
    class_name: ClassVar[str] = "Start"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Start

    hadActivity: Optional[Union[dict, Activity]] = None
    entity: Optional[Union[dict, Entity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.hadActivity is not None and not isinstance(self.hadActivity, Activity):
            self.hadActivity = Activity(**self.hadActivity)

        if self.entity is not None and not isinstance(self.entity, Entity):
            self.entity = Entity(**self.entity)

        super().__post_init__(**kwargs)


@dataclass
class Usage(InstantaneousEvent):
    """
    Usage is the beginning of utilizing an entity by an activity. Before usage, the activity had not begun to utilize
    this entity and could not have been affected by the entity.@en
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV.Usage
    class_class_curie: ClassVar[str] = "prov:Usage"
    class_name: ClassVar[str] = "Usage"
    class_model_uri: ClassVar[URIRef] = LINKML_PROV.Usage

    entity: Optional[Union[dict, Entity]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.entity is not None and not isinstance(self.entity, Entity):
            self.entity = Entity(**self.entity)

        super().__post_init__(**kwargs)


# Enumerations


# Slots

