from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from . import get_db
from loguru import logger
from src.db.models import EmployeeInfo
from typing import Optional

router = APIRouter()


class EmployeeCreate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    department: Optional[str] = None


@router.get("/get_all_emp_info", tags=["View Employees"])
def get_all_emp_data(
        db: Session = Depends(get_db)
):
    try:
        res = db.query(EmployeeInfo).all()
        return {
            "status_code": 200,
            "detail": res
        }
    except Exception as e:
        logger.debug(f"Error Occurred in get_all_emp_data - {e}")
        raise HTTPException(status_code=500, detail=f"{e}")


@router.get("/get_emp_info_by_id", tags=["View Employees"])
def get_emp_by_id(
        id: int,
        db: Session = Depends(get_db)
):
    try:
        res = db.query(EmployeeInfo).filter_by(id=id).all()
        return {
            "status_code": 200,
            "detail": res
        }
    except Exception as e:
        logger.debug(f"Error Occurred in get_emp_by_id - {e}")
        raise HTTPException(status_code=500, detail=f"{e}")


@router.post("/add_new_employee", tags=["Manage Employee"])
def add_emp_info(
        info: EmployeeCreate,
        db: Session = Depends(get_db)
):
    try:
        emp_name = info.name
        stud_exits = db.query(EmployeeInfo).filter_by(name=emp_name).all()
        if len(stud_exits) > 0:
            logger.debug(f"Student information is already exists of Name - {emp_name}")
            raise HTTPException(status_code=400, detail=f"Student Name - {emp_name} information already exists")
        else:
            emp_add_info = EmployeeInfo(
                name=emp_name,
                email=info.email,
                address=info.address,
                department=info.department
            )
            db.add(emp_add_info)
            db.commit()
            return {
                "status_code": 200,
                "detail": f"Employee Name - {emp_name} Information Added Successfully"
            }
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.debug(f"Error Occurred in add_emp_info - {e}")
        raise HTTPException(status_code=500, detail=f"{e}")


@router.put("/update_employee_info", tags=["Manage Employee"])
def modify_emp_info(
        id: int,
        info: EmployeeCreate,
        db: Session = Depends(get_db)
):
    try:
        emp_name = info.name
        update_stud_info = db.query(EmployeeInfo).filter_by(id=id).update(info.dict(exclude_unset=True))
        if update_stud_info:
            db.commit()
            return {
                "status_code": 200,
                "detail": f"Employee Name - {emp_name} Information Modified Successfully"
            }
        else:
            logger.debug(f"Employee information not exists of Name - {emp_name}")
            raise HTTPException(status_code=400, detail=f"Employee Name - {emp_name} information not exists")
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.debug(f"Error Occurred in modify_emp_info - {e}")
        raise HTTPException(status_code=500, detail=f"{e}")


@router.delete("/delete_employee", tags=["Manage Employee"])
def delete_emp_info(
        id: int,
        db: Session = Depends(get_db)
):
    try:
        res = db.query(EmployeeInfo).filter_by(id=id).all()
        if len(res) > 0:
            db.delete(res[0])
            db.commit()
            return {
                "status_code": 200,
                "detail": f"Employee id - {id} Information Deleted Successfully"
            }
        else:
            logger.debug(f"Employee information not exists of Employee id - {id}")
            raise HTTPException(status_code=400, detail=f"Employee id - {id} information not exists")
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.debug(f"Error Occurred in delete_emp_info - {e}")
        raise HTTPException(status_code=500, detail=f"{e}")
