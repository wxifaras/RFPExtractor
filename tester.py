import datetime
import uuid
from cosmos_db_service import cosmos_db_service
from datetime import datetime, timezone

rfp_id = str(uuid.uuid4())
currentDate = str(datetime.now(timezone.utc))

rfp_staffing_extract = {
    "id": rfp_id,
    "doc_type": "rfp_staffing_extract",
    "extract_date": currentDate,
    "blob_names": "",
    "required_roles": "",
    "role_requirements": "",
    "resume_requirements": "",
}

service = cosmos_db_service()
service.initialize()
created_item = service.insert_rfp_staffing_extract(rfp_staffing_extract)

print(created_item)