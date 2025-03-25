from flask import request,make_response
import datetime,json
from db import db,app
from model import Leavereq
from sqlalchemy import func

#api call to add leave request
@app.route('/leave-requests',methods=['POST'])
def leave_request(request):
    employee_id=request.data.get('employee_id')
    start_date=request.data.get('start_date')
    end_date=request.data.get('end_date')
    leave_type=request.data.get('leave_type')
    reason=request.data.get('reason')

    if not employee_id:

        return make_response(
            {
            "error":"Invalid request"
            },400
        )
    else:
        if not validate_date(start_date,end_date):
            return make_response(
                {
                  "error":"end_date must be after start_date",
                  "message:":"maximum consecutive leave days is 14"
                },
                400
            )
        elif not validate_status(leave_type):
            return make_response(
                {
                    "message":"Invalid request"
                },400
            )
        else:
            employee=Leavereq(
                employee_id=employee_id,
                start_date=start_date,
                end_date=end_date,
                leave_type=leave_type,
                reason=reason,
                created_at=func.current_timestamp()
            )
        db.session.add(employee)
        db.session.commit(employee)
        
    return make_response(
            {"message":"Leave request added"},200)

#api call to fecth required empi leave details
@app.route('/leave-requests/emp_id',methods=['GET'])
def view_leavereq(request):
    empid=request.data.get('employee_id')
    if empid:
        result=Leavereq.query.fetchall(empid=empid)
        return make_response(
            {"result":result},200
        )
    else:
        return make_response(
            {"message":"Emp id request not found"},
            400
        )

#function to validate date
def validate_date(start_dt,end_dt):

    if start_dt < end_dt:
        #checking if maximum consecutive leave exceeds
        if (end_dt-start_dt)>14:
            print("maximum consecutive leave exceeds")
            return False
        else:
            return True
    else:
        return False

#function to validate status of leave request 
def validate_status(status):
    lst=['ANNUAL','SICK','PERSONAL']
    if status in lst:
        return True
    else:
        return False
    










