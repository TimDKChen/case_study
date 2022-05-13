from app import api
from flask_restplus import fields

property_ori = api.model('property_ori', {
    "Lots": fields.String(example="Lot 3 Sec 3162 DP 51741 Hd of Munno P"),
    "Address": fields.String(example="8  Adaluna Crescent"),
    "Suburb_PostCode": fields.String(example="SMITHFIELD  SA  5114"),
    "Suburb": fields.String(example="SMITHFIELD"),
    "Street": fields.String(example="Adaluna Crescent"),
    "PostCode": fields.String(example="5114"),
})

property_details = api.model('property_details', {
    "id": fields.Integer(example=0),
    "Lots": fields.String(example="Lot 3 Sec 3162 DP 51741 Hd of Munno P"),
    "Address": fields.String(example="8  Adaluna Crescent"),
    "Suburb_PostCode": fields.String(example="SMITHFIELD  SA  5114"),
    "Suburb": fields.String(example="SMITHFIELD"),
    "Street": fields.String(example="Adaluna Crescent"),
    "PostCode": fields.String(example="5114"),
})
